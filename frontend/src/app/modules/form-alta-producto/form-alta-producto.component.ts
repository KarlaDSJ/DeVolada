import { Component, OnInit } from '@angular/core';
import { AdminProductoService } from '../../services/admin-producto.service';
import { ProductosService } from '../../services/productos.service';
import { CookieService } from 'ngx-cookie-service';
import Swal from 'sweetalert2';
import { Output, EventEmitter, ViewChild, AfterViewInit, ElementRef} from '@angular/core';
import { Directive, HostListener } from '@angular/core';

@Component({
  selector: 'app-form-alta-producto',
  templateUrl: './form-alta-producto.component.html',
  styleUrls: ['./form-alta-producto.component.css']
})


export class FormAltaProductoComponent implements OnInit {

  

  datosProducto = {
    idProducto : 0,
    correo: '',
    nombre: '',
    precio: 0.00,
    disponibles: 1,
    descripcion: '',
    categorias: "",
    imagenes: []
  }

  respuesta = { 
    error: null,
    mensaje: null
  }

  datosModal= {
    titulo: '',
    boton_confirmar: '',
    texto_accion: ''
  }

  datosModalSubir= {
    titulo: 'Formato para dar de alta producto',
    boton_confirmar: 'dar de alta',
    texto_accion: 'dar de alta'
  }

  datosModalActualizar= {
    titulo: 'Formato para actualizar producto',
    boton_confirmar: 'guardar cambios',
    texto_accion: 'actualizar'
  }

  aceptarTerminos = false

  @Output() productoDadoAltaEvent = new EventEmitter();

  constructor( private _adminService: AdminProductoService, 
               private _productosService: ProductosService, 
               private _cookie: CookieService ){}


  ngOnInit(): void {
    // Obtiene el correo del vendedor
    const correo = this._cookie.get('token_accessV')
    this.datosProducto.correo = correo
    this.configuraModalAltaProducto()
  }


  @ViewChild('modalAltaProducto') modalAltaProducto: any;
  cierraModal() {
    this.modalAltaProducto.nativeElement.click();
    this.reseteaFormulario();
  }

  abreModal() {
    console.log(this.modalAltaProducto)
    //this.modalAltaProducto.open();
  }


  configuraModalAltaProducto(){
    this.datosModal = this.datosModalSubir;
    this.reseteaFormulario()
  }

  configuraModalActualizaProducto(){
    this.datosProducto.idProducto = this._adminService.get_Producto_seleccionado();
    console.log("KARLA:", this.datosProducto.idProducto)
    this.datosModal = this.datosModalActualizar;
    this.reseteaFormulario()
    this.cargaDatosProducto(this.datosProducto.idProducto)
  }

  // Carga los datos del producto con el id especificado al formulario 
  cargaDatosProducto(idProducto){
    this._productosService.getProducto( idProducto ).subscribe(respuesta => {
      console.log("Datos del producto <", idProducto, "> cargados:", respuesta)
      this.datosProducto.nombre = respuesta.nombre.valueOf();
      this.datosProducto.precio = respuesta.precio;
      this.datosProducto.disponibles = respuesta.disponibles;
      this.datosProducto.descripcion = respuesta.descripcion.valueOf();
      for( let categoria of respuesta.categoria ){
        this.datosProducto.categorias += categoria.categoria.valueOf() +", ";
      }
        
    } )
  }

  // Resetea los datos del formulario
  reseteaFormulario(){
    this.datosProducto.nombre = ""
    this.datosProducto.precio = 0
    this.datosProducto.disponibles = 1
    this.datosProducto.descripcion = ""
    this.datosProducto.categorias = ""
    this.datosProducto.imagenes = []
    this.aceptarTerminos = false
  }
  

  // Sube un nuevo producto a la BD
  async daAltaProducto() {

    console.log(this.datosProducto)

    // Hace la petición para agregar los datos del nuevo producto a la tabla Producto
    this._adminService.daAltaProducto(this.datosProducto).subscribe(respuesta => {
      if ( respuesta.error != undefined){

        // Informa al usuario en caso de error con un mensaje
        this.respuesta.error = respuesta.error 
        this.respuesta.mensaje = respuesta.mensaje
        Swal.fire({icon: 'error', title: 'Ups!', text: this.respuesta.mensaje })
        
      }
      else {

        // Actualiza el idProducto por el nuevo id generado del producto creado
        this.datosProducto.idProducto = respuesta.idProducto

        // Sube las categorias del producto a la BD
        this.subeCategoriasProducto(this.datosProducto.idProducto)

        // Sube las imagenes del producto a la BD
        this.subeImagenesProductos(this.datosProducto.idProducto)

        // Manda un signal para que la página de mis productos sepa que se agregó un nuevo producto.
        this.productoDadoAltaEvent.emit()

        // Informa al usuario que el producto se dió de alta correctamente con un mensaje.
        Swal.fire({icon: 'success', title: 'Éxito', text: 'Tu producto se ha dado de alta correctamente.'})
        this.cierraModal()
      }
    } ) 
  }


  // Actualiza y/o agrega las categorias del producto en la BD por las categorias indicadas por el usuario
  async subeCategoriasProducto(idProducto){
    var categorias_list = this.datosProducto.categorias.split(",")
    var categorias_json: any = { "categorias": categorias_list }

    // Hace la petición para actualizar las categorias del producto en la BD
    this._adminService.actualizaCategorias(idProducto, categorias_json).subscribe(respuesta => {
      console.log(respuesta)
    } ) 
  }

  // Actualiza y/o agrega las imagenes del producto en la BD.
  subeImagenesProductos(idProducto){
    this._adminService.subeImagenes( idProducto, this.datosProducto.imagenes )
        .subscribe(respuesta => {
          console.log("respuesta: ", respuesta)
        } )
  }

  // Acción de click en el botón submit
  submit(){
    // Verifica que los terminos y condiciones estén aceptados
    if ( !this.aceptarTerminos){
      Swal.fire({icon: 'warning', 
                 title: '¡Espera!', 
                 text: "Para poder dar de alta tu producto debes aceptar los términos y condiciones" })
      return;
    }

    // Verifica que al menos una imagen haya sido agregada
    if ( this.datosProducto.imagenes.length == 0){
      Swal.fire({icon: 'warning', 
                 title: 'Ups!', 
                 text: "No has añadido ninguna imagen a tu producto" })
      return;
    }

    console.log( "Se intentaran subir las imagenes")
    console.log( this.datosProducto.imagenes[0].file )
    

    this.daAltaProducto()
     
  }

  // On file Select
  onChange(event) {
    let imagenes = event.target.files;
    if (imagenes) {
      for (let img of imagenes) {
        let reader = new FileReader();
        reader.onload = (e: any) => {
          this.datosProducto.imagenes.push( 
            { "file": img,
              "img": e.target.result });
        }
        reader.readAsDataURL(img);
      }
    }
  }



    // Acción de click en el botón upload
    eliminaImg(img_index) {
      this.datosProducto.imagenes.splice(img_index,1);
  }

}
