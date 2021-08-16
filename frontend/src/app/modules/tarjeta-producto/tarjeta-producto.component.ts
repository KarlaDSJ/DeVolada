import { Component, OnInit, Input } from '@angular/core';
import { IProducto } from "../../services/productos.service";

@Component({
  selector: 'app-tarjeta-producto',
  templateUrl: './tarjeta-producto.component.html',
  styleUrls: ['./tarjeta-producto.component.css']
})
export class TarjetaProductoComponent implements OnInit {

  @Input() producto: IProducto;

  calificacion = 3;
  cantidad_resenas = 0;
  estrellas_doradas = "";
  estrellas_restantes = "";

  constructor() { }

  ngOnInit(): void { 
    this.calculaEstrellas(this.calificacion)
  }


  calculaEstrellas(calificacion){
    calificacion = Math.round(calificacion)
    if (calificacion > 5) calificacion = 5;
    if (calificacion < 0) calificacion = 0;
    this.estrellas_doradas = "";
    for( let i=0; i< calificacion; i++) 
      this.estrellas_doradas += "★";
    for( let i=calificacion; i< 5; i++) 
      this.estrellas_restantes += "★";
  }

}
