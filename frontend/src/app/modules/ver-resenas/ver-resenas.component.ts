import { Component, Input, OnInit } from '@angular/core';
import { ResenasService, IResena } from "../../services/resenas.service";
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-ver-resenas',
  templateUrl: './ver-resenas.component.html',
  styleUrls: ['./ver-resenas.component.css']
})

/**
 * Clase para el funcionamiento del componente Ver Resenas
 */
export class VerResenasComponent implements OnInit {

  // Datos que vamos a ocupar, solo las inicializamos
  resenias: IResena[];
  id : string;
  promedio : number;
  total: number;
  

  /**
   * Constructor de la clase
   * @param _ResenasService varible del servicio de resenas para ver todas las reseñas de un producto
   * @param cookie cookie que manda el servidor para mantener la sesión
   */
  
  constructor(private _ResenasService: ResenasService,
              private cookie:CookieService) {}
  

  /**
   * Constructor que se inicializa cada que se carga el componente,
   * para obtener el promedio, # total, y todas las resenas de un 
   * producto.
   */            
  
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
