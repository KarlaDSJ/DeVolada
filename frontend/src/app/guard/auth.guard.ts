import { Injectable } from '@angular/core'; //inyectable
import { CanActivate } from '@angular/router'; //guardia
import { Router } from '@angular/router'; //ruta
import { CookieService } from 'ngx-cookie-service'; //cookie
import Swal from 'sweetalert2'; //mesajes bonitos


@Injectable({
  providedIn: 'root'
})

/** 
 * Guardia que revisa si el usuario inioió sesión como comprador, si fue así,
 * solo puede acceder a las funciones de comprador entonces solo puede acceder
 * con la directiva canActive, para que funcione tiene que pasarse a los parametros
 * de la ruta en app-routing.module.ts
*/

export class AuthGuard implements CanActivate {

  /**
   * Contructor del guardia
   * @param router la ruta a la cual se va a redirijir si es que no ha iniciado sesión
   * @param cookie utilizamos las cookies para ver si es que ha iniciado sesion como comprador
   */
  
  constructor(private router:Router, private cookie:CookieService){}
  
  /**
   * Función para redirigir al usaario si no ha iniciado sesión
   * @param flag 
   */
  
  redirect(flag:boolean):any{
    if(!flag){
      Swal.fire({icon:'error',
      title:'Error',
      text: 'Tienes que iniciar sesión primero'})
      this.router.navigate(['/'])
    }
  }

  /**
   * Función para saber si existe la cookie, si fue asi entonces quiere decir que 
   * si inició sesión como comprador, asi que va poder acceder a las funcionalidades 
   * del comprador
   * @returns verdadero si puede acceder a las funncionalidades, falso en otro caso
   */
  
  canActivate():boolean{
    const cookie = this.cookie.check('token_accessC')
    console.log(cookie)
    this.redirect(cookie)
    return cookie;
  }
  
}
