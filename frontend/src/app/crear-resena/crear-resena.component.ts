import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ResenasService, IInfoProducto } from "../resenas.service";
import { IResena } from "../resenas.service";
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-crear-resena',
  templateUrl: './crear-resena.component.html',
  styleUrls: ['./crear-resena.component.css']
})
export class CrearResenaComponent implements OnInit {

  resenas :  IResena;
  listaT = ['★','★','★','★','★'];
  vtar = false;
  infoProducto: IInfoProducto;

  correo = 'perritosalva@gmail.com';
  calificacion:any;
  opinion:any;


  constructor(private _route:ActivatedRoute, private _ResenasService: ResenasService) { 

  }

  ngOnInit(): void {
    this.infoProducto=this._ResenasService.getInfoProducto();
  }

  submit(f:NgForm) {
    this._ResenasService.crearResenas(this.infoProducto.idProducto,this.correo,this.opinion,this.calificacion)
    this.vtar = true
    console.log(f.value.calificacionElegida)
  }


}
