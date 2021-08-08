import { Component, Inject } from '@angular/core';
import { DOCUMENT } from '@angular/common';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'devolada';
  esComprador = true;


  constructor(@Inject(DOCUMENT) document: any) { 
    
    let url = 'http://localhost:4200'
    let url2 = 'http://localhost:33271'
    
    if (document.location.href == url+'/' || document.location.href == url+'/registrar' || document.location.href == url2+'/' || document.location.href == url2+'/registrar'){
      this.esComprador = false;
    } else{
      this.esComprador = true;
    }    
  }
}
