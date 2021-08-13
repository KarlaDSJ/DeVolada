import { Component, OnInit } from '@angular/core';
import { Router}   from '@angular/router';
import { ResenasService, IInfoProducto } from "../../services/resenas.service";
import { IResena } from "../../services/resenas.service";
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

  correo = 'zogilvie1w@ezinearticles.com';
  calificacion:any;
  opinion:any;


  constructor(private router: Router, private _ResenasService: ResenasService) { 
  }

  ngOnInit(): void {
    this.infoProducto=this._ResenasService.getInfoProducto(); 
  }

  submit(f:NgForm) {
    console.log(this.calificacion+"asdslkd");
    this.calificacion = 3;
    this._ResenasService.crearResenas(this.infoProducto.idProducto,this.correo,this.calificacion,this.opinion)
      .subscribe(data => { console.log(data);
        this.router.navigate(['/producto/'+this.infoProducto.idProducto]);
       });
    this.vtar = true
  }


}
