import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { ActivatedRoute } from '@angular/router';
import { LoginService } from './login.service';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { ILogin } from './login.service';

import { LoginComponent } from './login/login.component';

@Injectable({
  providedIn: 'root'
})



export class AuthGuard implements CanActivate {
  logeado : boolean;
  constructor(private loginservice:LoginService, private router:Router, private cookie:CookieService){

   }

   redirect(flag:boolean):any{
     if(!flag){
       this.router.navigate(['/'])
     }
   }
   canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
      const cookie = this.cookie.check('token_access')
      console.log(cookie)
      this.redirect(cookie)
      return cookie;
  }
  
}
