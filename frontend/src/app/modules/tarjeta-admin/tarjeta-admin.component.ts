import { Component, OnInit, Input } from '@angular/core';
import { AdminProductoService } from '../../services/admin-producto.service';
import { ProductosService } from '../../services/productos.service';
import { ResenasService, IInfoProducto } from "../../services/resenas.service";
import { Output, EventEmitter } from '@angular/core';
import Swal from 'sweetalert2';
import { IProducto } from "../../services/productos.service";

@Component({
  selector: 'app-tarjeta-admin',
  templateUrl: './tarjeta-admin.component.html',
  styleUrls: ['./tarjeta-admin.component.css']
})
export class TarjetaAdminComponent implements OnInit {

  @Input() producto: IProducto;

  ganancias = 0;
  calificacion = 0;

  constructor( private _adminService: AdminProductoService,
               private _productoService: ProductosService,
               private _resenaService: ResenasService ){}

  ngOnInit(): void {
    this.ganancias = this.producto.precio * this.producto.vendidos;
    // Carga la primer imagen del producto
    this._productoService.getImagenDecodificada(this.producto.idProducto).subscribe(respuesta => {
      this.producto.imagenes[0] = respuesta[0];
    })

    // Carga la calificacion promedio de las resenas del producto
    this._resenaService.obtenerPromedio(String(this.producto.idProducto)).subscribe(respuesta => {
        this.calificacion = respuesta.promedio;
    })
  }
  
  @Output() EliminarEvent = new EventEmitter();
  @Output() EditarEvent   = new EventEmitter();

  accionEditarProducto(idProducto){
    this._adminService.set_Producto_seleccionado(idProducto);
    this.EditarEvent.emit();
  }

  accionEliminarProducto(idProducto){
    Swal.fire({
      title: 'Estás seguro que quieres eliminar este producto?',
      text: "Esta acción es completamente irreversible",
      icon: 'warning',
      showCancelButton: true,
      reverseButtons: true,
      cancelButtonColor: '#868686',
      confirmButtonColor: '#ff4d4d',
      cancelButtonText: 'Cancelar',
      confirmButtonText: 'Sí, borralo'
    }).then((result) => {
      if (result.isConfirmed) {
        
        // Realiza la peticion para borrar el producto a la BS
        this._adminService.eliminaImagenesProducto(idProducto).subscribe(respuesta => {
          console.log(respuesta)
        })

        this._adminService.eliminaProducto(idProducto).subscribe(respuesta => {
          this.EliminarEvent.emit();
          console.log(respuesta)
          if ( respuesta.error == undefined){
            Swal.fire(
              'Borrado!',
              'El producto se ha dado de baja correctamente en el sistema.',
              'success'
            )
          } 
          else {
            Swal.fire(
              'Error',
              'Hubo un problema al procesar tu petición: ' + respuesta.mensaje ,
              'warning'
            )
          }
        } ) 
      }
    })
  }

}