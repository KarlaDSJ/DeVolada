import { Component, Input, OnInit } from '@angular/core';
import { ResenasService, IResena } from "../../services/resenas.service";
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-ver-resenas',
  templateUrl: './ver-resenas.component.html',
  styleUrls: ['./ver-resenas.component.css']
})
export class VerResenasComponent implements OnInit {

  resenias: IResena[];
  id : string;
  promedio : number;
  total: number;
  
  constructor(private _ResenasService: ResenasService, private cookie:CookieService) {
  }
  
  ngOnInit(): void {
    const idProducto = this.cookie.get('id')
    this._ResenasService.obtenerPromedio(idProducto).subscribe(respuesta => {
      this.promedio = respuesta.promedio;
    })
    this._ResenasService.obtenerTotal(idProducto).subscribe(respuesta => {
      this.total = respuesta.total;
    })
    this._ResenasService.mostrarResenas(idProducto)
    .subscribe(data => { 
      this.resenias = data;
      console.log(data);
    });
  }

}
