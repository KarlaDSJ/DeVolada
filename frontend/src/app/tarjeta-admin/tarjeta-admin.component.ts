import { Component, OnInit, Input } from '@angular/core';
import { AdminProductoService } from '../admin-producto.service';
import { IProducto } from '../productos.service';
import { Output, EventEmitter } from '@angular/core';
import Swal from 'sweetalert2';


@Component({
  selector: 'app-tarjeta-admin',
  templateUrl: './tarjeta-admin.component.html',
  styleUrls: ['./tarjeta-admin.component.css']
})
export class TarjetaAdminComponent implements OnInit {

  @Input() producto: IProducto;

  constructor( private _adminService: AdminProductoService ) { }

  ngOnInit(): void {}
  
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