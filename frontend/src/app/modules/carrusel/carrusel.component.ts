import { Component, OnInit, Input } from '@angular/core';
import { IProducto } from "../../services/productos.service";

@Component({
  selector: 'app-carrusel',
  templateUrl: './carrusel.component.html',
  styleUrls: ['./carrusel.component.css']
})
export class CarruselComponent implements OnInit {

  @Input() productos:IProducto[];
  responsiveOptions:any;

  constructor() { 
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
  }

}
