import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-barra-nav-vendedor',
  templateUrl: './barra-nav-vendedor.component.html',
  styleUrls: ['./barra-nav-vendedor.component.css']
})
export class BarraNavVendedorComponent implements OnInit {

  constructor( private _router:Router, private _cookie: CookieService) { }

  ngOnInit(): void {
  }

  logout(){
    this._cookie.deleteAll();
    this._router.navigate(['/'])
    
  }

}
