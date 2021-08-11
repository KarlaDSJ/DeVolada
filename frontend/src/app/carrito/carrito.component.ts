import { Component, OnInit } from '@angular/core';
import { CarritoService } from '../carrito.service';
import { CookieService } from 'ngx-cookie-service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-carrito',
  templateUrl: './carrito.component.html',
  styleUrls: ['./carrito.component.css']
})
export class CarritoComponent implements OnInit {

  idCarrito = -1;
  listaP = [];
  correo = "";

  /**
   * Obtiene el total del carrito 
   * @returns total 
   */
  public get total(): number {
    let totalP = 0
    this.listaP.forEach(element => {
      totalP += element.cant * element.precioP;
    });
    return totalP
  }

  /**
   * Aumenta la cantidad de un producto acorde a los disponibles. 
   * @param indice posición de la lista de productos en el carrito
   */
  aumentarCP(indice: number): void {
    if (this.listaP[indice].cant < this.listaP[indice].disp) {
      this._carritoService.cambiarCantidad(this.listaP[indice].idP, this.idCarrito, ++this.listaP[indice].cant)
        .subscribe()
    }
  }

  /**
   * Disminuye la cantidad de un producto. El límite es 1
   * @param indice posición de la lista de productos en el carrito
   */
  disminuirCP(indice: number): void {
    if (this.listaP[indice].cant > 1) {
      this._carritoService.cambiarCantidad(this.listaP[indice].idP, this.idCarrito, --this.listaP[indice].cant)
        .subscribe()
    }
  }

  /**
   * Elimina un producto
   * @param i posición de la lista de productos en el carrito
   */
  eliminarP(i: number): void {
    this._carritoService.eliminarProducto(this.listaP[i].idP, this.idCarrito)
      .subscribe()
    // Simulamos que se quita :D 
    this.listaP.splice(i, 1);
  }

  constructor(private _carritoService: CarritoService,
    private cookie: CookieService) {
  }

  async ngOnInit(): Promise<void> {
    this.correo = this.cookie.get('token_access');
    try {
      let datos = await this._carritoService.obtenerCarrito(this.correo)
      this.idCarrito = Number(datos.msg)
    } catch (error) {
      Swal.fire({
        icon: 'error',
        title: 'Carrito no encontrado'
      })
    }

    try {
      let productos = await this._carritoService.obtenerProductos(this.idCarrito);
      this.listaP = productos.map(x => ({
        imagenp: x.imagenes[0].imagen,
        nombre: x.nombre,
        cant: x.cantidad,
        idP: x.idProducto,
        precioP: x.precio,
        disp: x.disponibles
      }))
    } catch (error) {
      Swal.fire({
        icon: 'error',
        title: 'No se pueden obtener tus productos'
      })
    }
  }

}
