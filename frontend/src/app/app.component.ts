import { Component, Inject } from '@angular/core';
import { DOCUMENT } from '@angular/common';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'devolada';
  esComprador = false;
  esVendedor = false;
  sinSesion = false;


  constructor(@Inject(DOCUMENT) document: any , private _cookie: CookieService) { 
    
    let url = 'http://localhost:4200'
    let url2 = 'http://localhost:33271'
    
    if(this._cookie.check('token_accessC')){
      
      
      this.esComprador = true
    }
    if(this._cookie.check('token_accessV')){
      this.esVendedor = true;
    }
    if(!this._cookie.check('token_accessC') == !this._cookie.check('token_accessV') ){
      this.sinSesion = true;
    }
    
    
    

    /*
    if (document.location.href == url+'/' || document.location.href == url+'/registrar' || document.location.href == url2+'/' || document.location.href == url2+'/registrar'){
      this.esComprador = false;
    } else{
      this.esComprador = true;
    }
  */    
  }

  
}
