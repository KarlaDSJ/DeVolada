import { Component, OnInit } from '@angular/core';
import { ILogin } from '../../services/login.service';
import { LoginService } from "../../services/login.service";
import { Router}   from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

/**
 * Clase para el funcionamiento del componente Login del comprador y del vendedor
 */

export class LoginComponent implements OnInit {

  // Datos que vamos a ocupar, solo las inicializamos

  login : ILogin;
  datos = '';
  sesion = '';
  nombre = '';
   
  //Diccionario con datos del comprador

  dataC ={
  correoC:'',
  contraseniaC:''
  }

  //Diccionario con datos del vendedor

  dataV ={
    correoV:'',
    contraseniaV:''
    }

  /**
   * Constructor de la clase
   * @param _loginService varible del servicio del login para poder subsribirse a este servicio
   * @param router uan rata para dirigir a otra ruta si es necesario
   * @param cookieServive la cookie que manda el servidor para mantener la sesión
   */

  constructor(  private _loginService: LoginService, 
                private router: Router,
                private cookieServive: CookieService){}
    
  /**
   * Constructor que se incializa cada que se carga el componente
   */

  ngOnInit(): void {}
    
  /**
   * Funcion que se subscribe al servicio de login para enviar los datos del
   * comprador, si los datos no son correctos se manda mensaje. 
   */

  submitC(){
    this._loginService.IniciarSesionC(this.dataC).subscribe(response => { //nos subscribimos
      this.datos = response.msg;
      if (this.datos == 'error_datos'){
        Swal.fire({icon:'error',
        title: 'oooops',
        text: 'Los datos ingresados son incorectos'})
      }
      if(this.datos == 'error_contrasenia'){
        Swal.fire({icon:'error',
        title: 'oooops',
        text: 'La contraseña es incorrecta'})
      }
      if(this.datos == 'success'){       
        this.sesion = response.session;
        this.nombre = response.nombre;

        Swal.fire({icon:'success',
        title: 'Bienvenido de nuevo',
        text: this.nombre})

        this.cookieServive.set('token_accessC',response.session,1,'/')
        this.router.navigate(['/inicio']);
      }
    })
  }

   /**
   * Funcion que se subscribe al servicio de login para enviar los datos del
   * vendedor, si los datos no son correctos se manda mensaje. 
   */

  submitV(){
    this._loginService.IniciarSesionV(this.dataV).subscribe(response => {
      this.datos = response.msg;
      if (this.datos == 'error_datos'){
        Swal.fire({icon:'error',
        title: 'oooops',
        text: 'Los datos ingresados son incorectos'})
      }
      if(this.datos == 'error_contrasenia'){
        Swal.fire({icon:'error',
        title: 'oooops',
        text: 'La contraseña es incorrecta'})
      }
      if(this.datos == 'success'){
        this.sesion = response.session;
        this.nombre = response.nombre;
        Swal.fire({icon:'success',
        title: 'Bienvenido de nuevo',
        text: this.nombre} )
        this.router.navigate(['/mis-productos']);
        this.cookieServive.set('token_accessV',response.session,1,'/')
      }
    })
  }
}