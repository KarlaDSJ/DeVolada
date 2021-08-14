import { Component, OnInit } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { Output, EventEmitter } from '@angular/core';
import { ProductosService } from "../../services/productos.service";
import { IProducto } from "../../services/productos.service";

@Component({
  selector: 'app-mis-productos',
  templateUrl: './mis-productos.component.html',
  styleUrls: ['./mis-productos.component.css']
})


export class MisProductosComponent implements OnInit {

  constructor(private _productoService: ProductosService,  private _cookie: CookieService) { }

  @Output() EditarEvent = new EventEmitter();

  // Lista para almacenar los de productos del vendedor a mostrar
  lista_productos:IProducto[];

  // Correo del vendedor
  correo_vendedor = ""

  ngOnInit(): void {
    this.cargaCorreoVendedor()
    console.log("Accediendo a Mis productos para vendedor con correo <" + this.correo_vendedor + ">")
    this.cargaListaProductos()
  }

  // Carga la lista de productos del vendedor
  // Hace una peticion a la BS para obtenerlos 
  // Esta funcion debe ser llamada tras borrar, actualizar, agregar un nuevo producto y al inicio.
  cargaListaProductos(){
    this._productoService.obtenProductosVendedor(this.correo_vendedor)
          .subscribe(data => { this.lista_productos = data; }) 
  }

  accionEditarProducto(){
    this.EditarEvent.emit();
  }

  // Carga el correo del vendedor a través de las cookies.
  cargaCorreoVendedor(){
    this.correo_vendedor = this._cookie.get('token_access')
  }

}

