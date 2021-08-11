import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { LoginService } from '../services/login.service';
import Swal from 'sweetalert2';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Injectable({
  providedIn: 'root'
})
export class AuthVGuard implements CanActivate {
  
  
  constructor(private loginservice:LoginService, private router:Router, private cookie:CookieService){

  }

  redirect(flag:boolean):any{
    if(!flag){
      Swal.fire({icon:'error',
      title:'Error',
      text: 'Tienes que iniciar sesión primero'})
      this.router.navigate(['/'])
    }
  }
  canActivate(
   route: ActivatedRouteSnapshot,
   state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
     
     const cookie = this.cookie.check('token_accessV')
     
     console.log(cookie)
     this.redirect(cookie)
     return cookie;
 }
  
}
