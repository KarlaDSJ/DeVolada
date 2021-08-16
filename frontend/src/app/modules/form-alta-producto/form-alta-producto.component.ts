import { Component, OnInit } from '@angular/core';
import { AdminProductoService } from '../../services/admin-producto.service';
import { ProductosService } from '../../services/productos.service';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';
import { Output, EventEmitter, ViewChild } from '@angular/core';

@Component({
  selector: 'app-form-alta-producto',
  templateUrl: './form-alta-producto.component.html',
  styleUrls: ['./form-alta-producto.component.css']
})


export class FormAltaProductoComponent implements OnInit {

  // Indica si se ha presionado el checkbox para aceptar TyC
  aceptarTerminos = false;

  // Indica si la función del formulario será dar de alta o modificar un producto.
  modoSubeProducto = true;

  // Contiene los datos del producto en el formulario.
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

  // Almacena los datos de respuesta al hacer peticiones para mostrarlas en mensajes.
  respuesta = { 
    error: null,
    mensaje: null
  }

  // Datos que el modal mostrará dependiendo de si se subirá/actualizará el producto.
  datosModal= {
    titulo: '',
    boton_confirmar: ''
  }

  // Datos a mostrar en el modal cuando la función es subir el producto.
  datosModalSubir= {
    titulo: 'Formato para dar de alta producto',
    boton_confirmar: 'finalizar'
  }

  // Datos a mostrar en el modal cuando la función es actualizar el producto.
  datosModalActualizar= {
    titulo: 'Formato para actualizar producto',
    boton_confirmar: 'actualizar'
  }


  // Signal que el formulario lanza cuando se sube o modifica un producto 
  // para que la página recarge la información de las tarjetas de producto de admin.
  @Output() productoDadoAltaEvent = new EventEmitter();

  constructor( private _adminService: AdminProductoService, 
               private _productosService: ProductosService, 
               private _cookie: CookieService,
               private router: Router){}


  // Función que se ejecuta al cargar la página. Obtiene el correo del vendedor a través de la sesión.
  ngOnInit(): void {
    const correo = this._cookie.get('token_accessV') // Obtiene el correo del vendedor
    this.datosProducto.correo = correo
    this.configuraModalAltaProducto() // Configura por default al modal para subir productos.
  }


  @ViewChild('modalAltaProducto') modalAltaProducto: any;
  cierraModal() {
    this.modalAltaProducto.nativeElement.click();
    this.reseteaFormulario();
  }


  // Configura al modal para que su función sea la de dar de alta un producto
  configuraModalAltaProducto(){
    this.modoSubeProducto = true;
    this.datosModal = this.datosModalSubir;
    this.reseteaFormulario()
  }

  // Configura al modal para que su función sea la de actualizar un producto
  configuraModalActualizaProducto(){
    this.modoSubeProducto = false;
    this.datosProducto.idProducto = this._adminService.get_Producto_seleccionado();
    this.datosModal = this.datosModalActualizar;
    this.reseteaFormulario()
    this.cargaDatosProducto(this.datosProducto.idProducto)
  }

  // Carga al formulario los datos del producto según el id especificado
  cargaDatosProducto(idProducto){

    // Carga los datos básicos del producto
    this._productosService.getProducto( idProducto ).subscribe(respuesta => {
      console.log("Datos del producto <", idProducto, "> cargados:", respuesta)
      this.datosProducto.nombre = respuesta.nombre.valueOf();
      this.datosProducto.precio = respuesta.precio;
      this.datosProducto.disponibles = respuesta.disponibles;
      this.datosProducto.descripcion = respuesta.descripcion.valueOf();

      // Carga las categorias del producto
      for( let categoria of respuesta.categoria )
        this.datosProducto.categorias += categoria.categoria.valueOf() +", ";

      // Carga las imágenes del producto
      this._productosService.getImagenesDecodificadas( idProducto ).subscribe((respuesta: any[]) => {
        for( let img of respuesta)
          this.datosProducto.imagenes.push( img.imagen );
      } ) 
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
  

  // Hace la petición al service para subir un nuevo producto a la BD.
  subeProducto() {

    console.log("Subiendo producto: ", this.datosProducto)

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


  // Hace la petición al service para actualizar el producto en la BD.
  actualizaProducto() {

    console.log("Actualizando producto: ", this.datosProducto)

    // Hace la petición para agregar los datos del nuevo producto a la tabla Producto
    this._adminService.actualizaProducto(this.datosProducto).subscribe(respuesta => {
      if ( respuesta.error != undefined){

        // Informa al usuario en caso de error con un mensaje
        this.respuesta.error = respuesta.error 
        this.respuesta.mensaje = respuesta.mensaje
        Swal.fire({icon: 'error', title: 'Ups!', text: this.respuesta.mensaje })
        
      }
      else {

        // Sube las categorias del producto a la BD
        this.subeCategoriasProducto(this.datosProducto.idProducto)

        // Sube las imagenes del producto a la BD
        this.subeImagenesProductos(this.datosProducto.idProducto)

        // Manda un signal para que la página de mis productos sepa que se modificó un producto.
        this.productoDadoAltaEvent.emit()

        // Informa al usuario que el producto se dió de alta correctamente con un mensaje.
        Swal.fire({icon: 'success', title: 'Éxito', text: 'Los cambios de tu producto se han guardado correctamente.'})
        this.cierraModal()
        //this.router.navigate(['/mis-productos'])
      }
    } ) 
  }


  // Hace la petición al service para actualizar y/o agrega las categorias del producto en la BD.
  subeCategoriasProducto(idProducto){
    var categorias_list = this.datosProducto.categorias.split(",")
    var categorias_json: any = { "categorias": categorias_list }

    // Hace la petición para reemplazar y/o agregar las categorias del producto en la BD
    this._adminService.actualizaCategorias(idProducto, categorias_json).subscribe(respuesta => {
      console.log(respuesta)
    } ) 
  }

  // Hace la petición al service para reemplazar y/o agregar las imágenes del producto en la BD.
  subeImagenesProductos(idProducto){
    // Reemplaza las imagenes del producto por las actuales en el formulario.
    this._adminService.actualizaImagenes( idProducto, this.datosProducto.imagenes ).then(respuesta => {
          console.log(respuesta)
        } )
  }

  // Acción de click en el botón submit del formulario 
  submit(){
    // Verifica que los terminos y condiciones estén aceptados y si no muestra un mensaje
    if ( !this.aceptarTerminos){
      Swal.fire({icon: 'warning', 
                 title: '¡Espera!', 
                 text: "Para poder continuar debes aceptar los términos y condiciones" })
      return;
    }

    // Verifica que al menos una imagen haya sido agregada y si no muestra un mensaje
    if ( this.datosProducto.imagenes.length == 0){
      Swal.fire({icon: 'warning', 
                 title: 'Ups!', 
                 text: "No has añadido ninguna imagen a tu producto" })
      return;
    }

    // Verifica que al menos una categoria haya sido agregada y si no muestra un mensaje
    if ( this.datosProducto.categorias.replace(/\,/gi, '').trim() == "" ){
      Swal.fire({icon: 'warning', 
                 title: 'Ups!', 
                 text: "No has añadido ninguna categoria a tu producto" })
      return;
    }

    // Decide si va a lanzar una petición para dar de alta el producto o para modificarlo
    if ( this.modoSubeProducto )
      this.subeProducto()
    else 
      this.actualizaProducto()
     
  }

  // Carga las imagenes que el usuario selecciona en la ventana de archivos
  // Las agrega localmente a la lista de imágenes del formulario para 
  // después enviarlas a la petición.
  onChange(event) {
    let imagenes = event.target.files;
    if (imagenes) {
      for (let img of imagenes) {
        let reader = new FileReader();
        reader.onload = (e: any) => {
          this.datosProducto.imagenes.push( e.target.result )
            //{ "file": img,  // Archivo de la imagen ( se utiliza para mandarlo a las peticiones )
            //  "img": e.target.result // Datos binarios de la imagen en (se utiliza para mostrarlo en la página) 
            //});
        }
        reader.readAsDataURL(img);
      }
    }
  }

    // Acción de click en el botón de cada imagen para eliminarla
    // Elimina la imagen de la lista de imagenes local según el índice recibido.
    eliminaImg(img_index) {
      this.datosProducto.imagenes.splice(img_index,1);
  }

}
