import { Component, OnInit } from '@angular/core';
import { ILogin } from '../login.service';
import { LoginService } from "../login.service";
import { ActivatedRoute } from '@angular/router';
import { Router}   from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {

  login : ILogin;
  dataC ={
  correoC:'',
  contraseniaC:''
  }

  dataV ={
    correoV:'',
    contraseniaV:''
    }
  
  constructor(private _route:ActivatedRoute, private _loginService: LoginService, private router: Router) { 
    
  }

  ngOnInit(): void {
   
 }
    

  submitC(){
    //console.log(this.data)
  this._loginService.IniciarSesionC(this.dataC).subscribe(response => {
  this.router.navigate(['/inicio']);
    })
  }

  submitV(){
    //console.log(this.data)
  this._loginService.IniciarSesionV(this.dataV).subscribe(response => {
  this.router.navigate(['/inicio']);
    })
  }





}
