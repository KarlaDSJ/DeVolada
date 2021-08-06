import { Component, OnInit } from '@angular/core';
import { ILogin } from '../login.service';
import { LoginService } from "../login.service";
import { ActivatedRoute } from '@angular/router';
import { Router}   from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {

  login : ILogin;
  datos = '';
  sesion = '';
  nombre = '';
  dataC ={
  correoC:'',
  contraseniaC:''
  }

  dataV ={
    correoV:'',
    contraseniaV:''
    }
  
  constructor(private _route:ActivatedRoute,
    private _loginService: LoginService, 
    private router: Router,
    private cookieServive: CookieService){}
    

  ngOnInit(): void {
   
 }
    

  submitC(){
    //console.log(this.data)
  this._loginService.IniciarSesionC(this.dataC).subscribe(response => {
    console.log(response)
    this.datos = response.msg;
    this.cookieServive.set('token_access',response.session,1,'/')
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
      this.router.navigate(['/inicio']);
        
    }
    })
    
  }

  submitV(){
    //console.log(this.data)
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
      this.router.navigate(['/inicio']);
    }
})
  }
}






