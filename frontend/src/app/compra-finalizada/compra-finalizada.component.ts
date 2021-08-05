import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import Swal from 'sweetalert2';
import { CarritoService, IProductoCarrito } from "../carrito.service";
import { DireccionCompradorService, IDirComprador } from '../direccion-comprador.service';

@Component({
  selector: 'app-compra-finalizada',
  templateUrl: './compra-finalizada.component.html',
  styleUrls: ['./compra-finalizada.component.css']
})
export class CompraFinalizadaComponent implements OnInit {

  comprador = "Yo merengues";  
  dir = "";
  idCompra: number;
  idCarrito = 1;
  idDir = -1;
  productos: IProductoCarrito[];
  listaP = [];



  constructor(private _route: ActivatedRoute,
    private _carritoService: CarritoService,
    private _direccionService: DireccionCompradorService) { }


  /*
    Incluye los productos en la compra 
  */
  async incluirProductosCompra() {
    this.listaP.map(item => {
      let producto = item.idP;
      let compra = this.idCompra;
      let cantidad = item.cant;
      this._carritoService.incluirProductos(producto, compra, cantidad)
        .then(
          data => {
            console.log(data);
          },
          error => {
            Swal.fire({
              title: 'No se pudo agregar a la compra',
              text: error.error.msg,
              icon: 'error'
            })
          })

    })
  }

  /*
    Guarda los productos en la listaP 
  */
  async guardarProductos() {
    this.listaP = this.productos.map(x => ({
      imagenp: x.imagenes[0].imagen,
      nombre: x.nombre,
      cant: x.cantidad,
      idP: x.idProducto,
      precioP: x.precio,
      disp: x.disponibles
    })
    )
  }

  ngOnInit(): void {
    this.idCompra = Number(this._route.snapshot.paramMap.get('idCompra'));
    this.idDir = Number(localStorage.getItem('devoladaIdDir'));

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


    this._carritoService.obtenerProductos(this.idCarrito).subscribe(
      data => {
        this.productos = data;
        this.guardarProductos().then(data => (
          this.incluirProductosCompra().then(data => (
            this._carritoService.limpiarCarrito(this.idCarrito).subscribe(
              data => (2),
              error => (
                Swal.fire({
                  title: error.msg,
                  icon: 'error'
                }))
            )
          ))
        ))
      })
  }


}
