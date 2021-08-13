import { Component, OnInit } from '@angular/core';
import { ILogin } from '../../services/login.service';
import { LoginService } from "../../services/login.service";
import { Router}   from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import Swal from 'sweetalert2';
import { FormBuilder, FormGroup, Validators} from '@angular/forms';
import { textChangeRangeIsUnchanged } from 'typescript';


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
  myForm: FormGroup;

  datos = '';
  sesion = '';
  nombre = '';

  esValidoCorreoC= false;
  esVacioCorreoC = true;
  esValidocontraseniaC = false;
  esVacioContraseniaC = true;

  esValidoCorreoV= false;
  esVacioCorreoV = true;
  esValidocontraseniaV = false;
  esVacioContraseniaV = true;
   
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
                private cookieServive: CookieService,
                public fb: FormBuilder){
this.myForm = this.fb.group({
  correoC : ['',[Validators.required, Validators.email]],
  contraseniaC : ['', [Validators.required, ]],
  correoV : ['',[Validators.required, Validators.email]],
  contraseniaV : ['', [Validators.required, ]]
})
  
                }
    
  /**
   * Constructor que se incializa cada que se carga el componente
   */

  ngOnInit(): void {}
    
  /**
   * Funcion que se subscribe al servicio de login para enviar los datos del
   * comprador, si los datos no son correctos se manda mensaje. 
   */

  submitC(){
    
    
    console.log(this.dataC)

    this._loginService.IniciarSesionC(this.dataC).subscribe(response => { //nos subscribimos
      this.datos = response.msg;
      if (this.datos == 'error_datos'){
        this.esVacioCorreoC = false;
        this.esValidoCorreoC = false;
        Swal.fire({icon:'error',
        title: 'oooops',
        text: 'Los datos ingresados son incorectos'})
      }
      if(this.datos == 'error_contrasenia'){
        this.esVacioCorreoC = false;
        this.esValidoCorreoC = true;

        this.esVacioContraseniaC = false
        



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
        this.cookieServive.set('nombre',this.nombre,1,'/')
        this.router.navigate(['/inicio']);
      }
    })
  }

   /**
   * Funcion que se subscribe al servicio de login para enviar los datos del
   * vendedor, si los datos no son correctos se manda mensaje. 
   */

  submitV(){
    console.log(this.dataV)
    this._loginService.IniciarSesionV(this.dataV).subscribe(response => {
      this.datos = response.msg;
      if (this.datos == 'error_datos'){
        this.esVacioCorreoV = false;
        this.esValidoCorreoV = false;
        Swal.fire({icon:'error',
        title: 'oooops',
        text: 'Los datos ingresados son incorectos'})
      }
      if(this.datos == 'error_contrasenia'){
        this.esVacioCorreoV = false;
        this.esValidoCorreoV = true;

        this.esVacioContraseniaV = false
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