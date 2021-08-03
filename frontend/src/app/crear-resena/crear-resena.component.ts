import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ResenasService } from "../resenas.service";
import { IResena } from "../resenas.service";

@Component({
  selector: 'app-crear-resena',
  templateUrl: './crear-resena.component.html',
  styleUrls: ['./crear-resena.component.css']
})
export class CrearResenaComponent implements OnInit {

  resenas :  IResena;

  idProducto:any;
  correo:any;
  calificacion:any;
  opinion:any;


  constructor(private _route:ActivatedRoute, private _ResenasService: ResenasService) { 

  }

  ngOnInit(): void {
  }

  submit() {
    this._ResenasService.crearResenas(this.idProducto,this.correo,this.opinion,this.calificacion)
  }
}
