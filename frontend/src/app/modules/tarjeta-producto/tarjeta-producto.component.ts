import { Component, OnInit, Input } from '@angular/core';
import { IProducto } from "../../services/productos.service";
import { ResenasService, IResena } from "../../services/resenas.service";

@Component({
  selector: 'app-tarjeta-producto',
  templateUrl: './tarjeta-producto.component.html',
  styleUrls: ['./tarjeta-producto.component.css']
})
export class TarjetaProductoComponent implements OnInit {

  @Input() producto: IProducto;

  promedio:number;
  estrellaA:string = ""; //Cadena con estrellas amarillas
  estrellaG:string = ""; //Cadena con estrellas amarillas
  total: number = 0; //número de opiniones

  constructor(private _ResenasService: ResenasService) { }

  ngOnInit(): void { 
    this._ResenasService.obtenerPromedio(""+this.producto.idProducto).subscribe(respuesta => {
      this.promedio = Math.floor(respuesta.promedio);
      for (let i = 0; i < this.promedio; i++) { this.estrellaA += "★"}
      for (let i = 0; i < 5 - this.promedio; i++) { this.estrellaG += "★"}

      this._ResenasService.obtenerTotal(""+this.producto.idProducto).subscribe(respuesta => {
        this.total = respuesta.total;
      })
    })
  }

}
