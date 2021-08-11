import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import Swal from 'sweetalert2';
import { CarritoService, IProductoCarrito } from "../../services/carrito.service";
import { DireccionCompradorService, IDirComprador } from '../../services/direccion-comprador.service';

@Component({
  selector: 'app-compra-finalizada',
  templateUrl: './compra-finalizada.component.html',
  styleUrls: ['./compra-finalizada.component.css']
})
export class CompraFinalizadaComponent implements OnInit {

  comprador = "Yo merengues";
  dir = "";
  idCompra: number;
  idCarrito = -1;
  idDir = -1;
  productos: IProductoCarrito[];
  listaP = [];

  constructor(private _route: ActivatedRoute,
    private _carritoService: CarritoService,
    private _direccionService: DireccionCompradorService,
    private cookie: CookieService) { }

  /*
    Guarda los productos en la listaP 
    Incluye los productos en la compra    
  */
  async guardarProductos() {
    this.listaP = this.productos.map(
      x => ({
        imagenp: x.imagenes[0].imagen,
        nombre: x.nombre,
        cant: x.cantidad,
        idP: x.idProducto,
        precioP: x.precio,
        disp: x.disponibles
      }))

    // Peticiones el paralelo
    await Promise.all(
      this.listaP.map(
        async (item) => {
          let producto = item.idP;
          let compra = this.idCompra;
          let cantidad = item.cant;
          this._carritoService.incluirProductos(producto, compra, cantidad)
            .then(
              data => { },
              error => {
                Swal.fire({
                  title: 'No se pudo agregar el producto ' + producto + ' a la compra',
                  text: error.error.msg,
                  icon: 'error'
                })
              })
        }))
  }

  async ngOnInit(): Promise<void> {
    this.idCompra = Number(this._route.snapshot.paramMap.get('idCompra'));
    this.idDir = Number(localStorage.getItem('devoladaIdDir'));
    let correo = this.cookie.get('token_access');

    try {
      let datos = await this._carritoService.obtenerCarrito(correo)
      this.idCarrito = Number(datos.msg)
    } catch (error) {
      Swal.fire({
        icon: 'error',
        title: 'Carrito no encontrado'
      })
    }

    this._direccionService.obtenerDireccion(this.idDir).subscribe(
      data => (
        this.dir = data.calle + " " + data.numero + ", " + data.colonia + ", " + data.ciudad + ", " + data.estado + ", " + data.cp
      ),
      error => (
        Swal.fire({
          title: 'Ocurrió un error con la dirección ',
          icon: 'error'
        })
      )
    )

    try {
      this.productos = await this._carritoService.obtenerProductos(this.idCarrito);
      await this.guardarProductos();
      this._carritoService.limpiarCarrito(this.idCarrito)
        .subscribe(s => { console.log("Carrito limpio") })
    } catch (error) {
      Swal.fire({
        title: error.msg,
        icon: 'error'
      })
    }
  }


}
