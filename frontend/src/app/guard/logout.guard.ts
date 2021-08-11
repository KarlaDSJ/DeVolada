import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { CookieService } from 'ngx-cookie-service';
import Swal from 'sweetalert2';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class LogoutGuard implements CanActivate {
  constructor(private router:Router, private cookie:CookieService){

}

  
  canActivate(
   route: ActivatedRouteSnapshot,
   state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
     
  if(this.cookie.check('token_accessC')){

    this.router.navigate(['inicio']);
    Swal.fire({ icon: 'error',
                title: 'Error',
                text: 'Primero tienes que cerrar sesión'

    })
    return false
  }     
  if(this.cookie.check('token_accessV')){ 
    
    this.router.navigate(['mis-productos']);
    Swal.fire({ icon: 'error',
    title: 'Error',
    text: 'Primero tienes que cerrar sesión'})
    
    return false
    ;}
 
  return true;
  }

}

 
 
