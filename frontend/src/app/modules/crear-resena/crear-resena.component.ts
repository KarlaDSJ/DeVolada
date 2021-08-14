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


  constructor(private router: Router, private _ResenasService: ResenasService, private cookie: CookieService) { 
  }
  
  ngOnInit(): void {
    this.infoProducto=this._ResenasService.getInfoProducto(); 
  }
  
  submit(f:NgForm) {
    console.log(this.calificacion+"asdslkd");
    const correo = this.cookie.get('token_accessC');
    this.calificacion = 3;
    this._ResenasService.crearResenas(this.infoProducto.idProducto,correo,this.calificacion,this.opinion)
      .subscribe(data => { console.log(data);
        this.router.navigate(['/producto/'+this.infoProducto.idProducto]);
       });
    this.vtar = true
  }


}
