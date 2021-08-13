import { Component, Input, OnInit } from '@angular/core';
import { ResenasService, IResena } from "../../services/resenas.service";
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-resenas',
  templateUrl: './resenas.component.html',
  styleUrls: ['./resenas.component.css']
})
export class ResenasComponent implements OnInit {

  resenias: IResena[];
  @Input() idProducto: string;


  constructor(private _ResenasService: ResenasService, private cookie:CookieService) {
  }
  
  
  ngOnInit(): void {
    this._ResenasService.mostrar5Resenas(this.idProducto)
    .subscribe(data => { 
      this.cookie.set('id', this.idProducto, 1, '/');
      this.resenias = data;
      console.log(data);
    });
  }

}
