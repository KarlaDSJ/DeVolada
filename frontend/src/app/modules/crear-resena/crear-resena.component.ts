import { Component, OnInit } from '@angular/core';
import { Router}   from '@angular/router';
import { ResenasService, IInfoProducto } from "../../services/resenas.service";
import { IResena } from "../../services/resenas.service";
import { NgForm } from '@angular/forms';
import { CookieService } from 'ngx-cookie-service';


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

  calificacion:any;
  opinion:any;
  calificacion1:any;
  calificacion2:any;
  calificacion3:any;
  calificacion4:any;
  calificacion5:any;
  currentRate = 6;
  

  constructor(private router: Router, private _ResenasService: ResenasService, private cookie: CookieService) { 
  }
  
  ngOnInit(): void {
    this.infoProducto=this._ResenasService.getInfoProducto(); 
  }

  submit(f:NgForm) {
    this.calificacion=this.randomInteger(1,5)
    const correo = this.cookie.get('token_accessC');
    this._ResenasService.crearResenas(this.infoProducto.idProducto,correo,this.calificacion,this.opinion)
    .subscribe(data => { console.log(data);
      this.router.navigate(['/producto/'+this.infoProducto.idProducto]);
      });
    this.vtar = true
  }

  randomInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }


}
