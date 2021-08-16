import { Component, OnInit } from '@angular/core';
import { Router}   from '@angular/router';
import { ResenasService, IInfoProducto } from "../../services/resenas.service";
import { IResena } from "../../services/resenas.service";
import { NgForm } from '@angular/forms';
import { CookieService } from 'ngx-cookie-service';
import Swal from 'sweetalert2';


@Component({
  selector: 'app-crear-resena',
  templateUrl: './crear-resena.component.html',
  styleUrls: ['./crear-resena.component.css']
})

/**
 * Clase para el funcionamiento del componente Crear una Reseña
 */
export class CrearResenaComponent implements OnInit {

  // Datos que vamos a ocupar, solo las inicializamos

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
  

  /**
   * Constructor de la clase
   * @param router una ruta para dirigir a otra ruta si es necesario
   * @param _ResenasService varible del servicio de resenas para crear una reseña
   * @param cookie cookie que manda el servidor para mantener la sesión
   */

  constructor(private router: Router, 
              private _ResenasService: ResenasService, 
              private cookie: CookieService) { 
  }
  

  /**
   * Constructor que se incializa cada que se carga el componente
   */
  ngOnInit(): void {
    this.infoProducto=this._ResenasService.getInfoProducto(); 
  }


 /**
   * Funcion que asigna la calificación a la reseña
   */
  califica(calificacion){
    this.calificacion=calificacion
  }


  /**
   * Funcion que se subscribe al servicio de resenas para enviar los datos de la reseña creada
   */

  submit(f:NgForm) {
    console.log(f)
    console.log(this.opinion)
    const correo = this.cookie.get('token_accessC');
    if(this.opinion!=""){
      this._ResenasService.crearResenas(this.infoProducto.idProducto,correo,this.calificacion,this.opinion)
      .subscribe(data => {
        Swal.fire({icon:'success',
        title: 'Perfecto',
        text: 'Reseña guardada con éxito'})
        this.router.navigate(['/producto/'+this.infoProducto.idProducto]);
        });
    }
    Swal.fire({icon:'error',
        title: 'oooops',
        text: 'Debes seleccionar una calificación y escribir un comentario, por favor'})
    this.vtar = true
  }

}
