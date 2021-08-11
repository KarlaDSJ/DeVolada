import { Component, OnInit } from '@angular/core';
import { ProductosService } from "../../services/productos.service";
import { IProducto } from "../../services/productos.service";

@Component({
  selector: 'app-mas-vendidos',
  templateUrl: './mas-vendidos.component.html',
  styleUrls: ['./mas-vendidos.component.css']
})
export class MasVendidosComponent implements OnInit {
  
  productos:IProducto[];

  constructor(private _productoService: ProductosService) { }

  ngOnInit(): void {
    //Nos regresa el top de productos más vendidos 
    this._productoService.getTop5()
          .subscribe(data => {
            this.productos = data;
          })
  }

}
