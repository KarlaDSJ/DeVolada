import { Component, OnInit } from '@angular/core';
import { ProductosService } from "../productos.service";
import { IProducto } from "../productos.service";


@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.css']
})

export class TodosComponent implements OnInit {

  productos:IProducto[];

  responsiveOptions:any;

    constructor(private _productoService: ProductosService) {
        //Opciones para hacer responsivo el carrusel de productos
        this.responsiveOptions = [
          {
            breakpoint: '1078px',
            numVisible: 3,
            numScroll: 2
          },
          {
            breakpoint: '840px',
            numVisible: 2,
            numScroll: 1
          },
          {
            breakpoint: '575px',
            numVisible: 1,
            numScroll: 1
          }];
    }


  ngOnInit(): void {
    //Nos regresa todos los productos
    this._productoService.getProductos()
          .subscribe(data => {
            this.productos = data;
          })
  }

}
