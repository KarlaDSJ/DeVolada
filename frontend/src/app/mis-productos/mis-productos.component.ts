import { Component, OnInit } from '@angular/core';
import { ProductosService } from "../productos.service";
import { IProducto } from "../productos.service";

@Component({
  selector: 'app-mis-productos',
  templateUrl: './mis-productos.component.html',
  styleUrls: ['./mis-productos.component.css']
})


export class MisProductosComponent implements OnInit {

  lista_productos:IProducto[];

  constructor(private _productoService: ProductosService) { }

  ngOnInit(): void {
    //Nos regresa el top de productos más vendidos 
    this._productoService.obtenProductosVendedor("aellsworthe3@cnbc.com")
          .subscribe(data => { this.lista_productos = data; }) 
  }


}

