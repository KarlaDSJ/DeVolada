import { Component, Input, OnInit } from '@angular/core';
import { ResenasService, IResena } from "../../services/resenas.service";
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-resenas',
  templateUrl: './resenas.component.html',
  styleUrls: ['./resenas.component.css']
})

/**
 * Clase para el funcionamiento de ver las calificaciones globas 
 * de un producto y las primeras 5 reseñas de éste.
 */

export class ResenasComponent implements OnInit {

  // Datos que vamos a ocupar, solo las inicializamos
  resenias: IResena[];
  @Input() idProducto: string;
  id: string;
  promedio: number;
  total: number;
  puede: boolean;


  /**
   * Constructor de la clase
   * @param _ResenasService varible del servicio de resenas para ver promedios globales y las 5 primeras reseñas, de un producto
   * @param cookie cookie que manda el servidor para mantener la sesión
   */

  constructor(private _ResenasService: ResenasService, private cookie: CookieService) {
  }


  /**
   * Constructor que se inicializa cada que se carga el componente,
   * para obtener el promedio, # total, y las primeras 5 reseñas
   * de un producto.
   */

  ngOnInit(): void {
    let correo = this.cookie.get('token_accessC');
    this.puede = true;   //se deshabilita la opción de escribir reseña
    this._ResenasService.obtenerPromedio(this.idProducto).subscribe(respuesta => {
      this.promedio = respuesta.promedio;
    })
    this._ResenasService.obtenerTotal(this.idProducto).subscribe(respuesta => {
      this.total = respuesta.total;
    })
    this._ResenasService.mostrar5Resenas(this.idProducto)
      .subscribe(data => {
        this.cookie.set('id', this.idProducto, 1, '/');
        this.resenias = data;
      });

    this._ResenasService.verificar(this.idProducto, correo).subscribe(data => {
      let bandera = data.msg
      if (bandera == 'si') {
        this.puede = false
      } else {
        this.puede = true
      }
    }, error => {
      console.log(error);
    });
  }

}
