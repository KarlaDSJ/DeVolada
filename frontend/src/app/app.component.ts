import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'devolada';
  esComprador = true;


  constructor(private router: Router) { 
    console.log(this.router.url);
    
    if (this.router.url == '/login' || this.router.url == '/registrar'){
      this.esComprador = false;
    }
  }
}
