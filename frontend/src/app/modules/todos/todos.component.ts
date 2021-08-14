import { Component, OnInit } from '@angular/core';
import { ProductosService } from "../../services/productos.service";
import { IProducto } from "../../services/productos.service";


@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.css']
})

export class TodosComponent implements OnInit {

  productos:IProducto[];
  total:number;

  constructor(private _productoService: ProductosService) {}


  ngOnInit(): void {
    //Nos regresa todos los productos
    this._productoService.getProductos()
          .subscribe(data => {
            this.productos = data;
            this.total = this.productos.length;
          })
  }

}
