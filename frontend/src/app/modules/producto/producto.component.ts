import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ProductosService, IProducto } from "../../services/productos.service";
import { ResenasService } from '../../services/resenas.service';
import { CarritoService } from '../../services/carrito.service';
import Swal from 'sweetalert2';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-producto',
  templateUrl: './producto.component.html',
  styleUrls: ['./producto.component.css']
})


export class ProductoComponent implements OnInit {

  info: any;
  producto: IProducto;
  id: any = "";
  responsiveOptions: any;
  // Cambiar por el carrito del comprador
  idCarrito = -1;

  deshabilitar() {
    if (this.producto.disponibles <= 0) {
      return true;
    }
    else
      return false;

  }

  agregar(): void {
    this._carritoService.agregarCarrito(this.id, this.idCarrito)
      .subscribe(
        data => {
          Swal.fire({
            text: data.msg,
            icon: 'success'
          })
        },
        error => {
          Swal.fire({
            title: 'No se puede agregar',
            text: error.error.msg,
            icon: 'error'
          })
        })
  }

  constructor(private _route: ActivatedRoute,
    private _productoService: ProductosService,
    private _carritoService: CarritoService,
    private _ResenasService: ResenasService,
    private cookie: CookieService) {

    //Opciones para hacer responsivo el carrusel de fotos del productos
    this.responsiveOptions = [
      {
        breakpoint: '1024px',
        numVisible: 1,
        numScroll: 1
      }
    ];
  }

  async ngOnInit(): Promise<void> {
    this.id = this._route.snapshot.paramMap.get('id');
    //Nos regresa todos los productos
    this._productoService.getProducto(this.id)
      .subscribe(data => {
        this.producto = data;
        this.info = { 'idProducto': this.producto.idProducto, 'nombre': this.producto.nombre, 'imagen': this.producto.imagenes[0].imagen }
        this._ResenasService.setInfoProducto(this.info)
      })
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
  }

}
