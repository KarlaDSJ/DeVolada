import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

export interface IadminProducto{
  idProducto: number,
  nombre: String;
  precio: number;
  descripcion: String;
  disponibles: number;
  imagenes: { imagen: String }[];
  categorias: String[];
  
  // Repuesta por parte del sever tras hacer la petición
  error: number,
  mensaje: String
}

export interface ICategoria {
  categoria: String
}

@Injectable({
  providedIn: 'root'
})
export class AdminProductoService {

  private _url = 'http://127.0.0.1:5000/'

  constructor( private _http: HttpClient ) {}

  daAltaProducto( datosProducto : {correo: string, 
                                   nombre: string, 
                                   precio:number, 
                                   descripcion: string , 
                                   disponibles:number} ): Observable<IadminProducto> {
    return this._http.post<IadminProducto>(this._url+"/producto", datosProducto);
  }

  agregaCategorias( categorias : {categorias : string} )  {
    return this._http.post<IadminProducto>(this._url+"/categorias", categorias);
  }


  // Returns an observable
  upload(imagen):Observable<any> {
  
    // Create form data
    const formData = new FormData(); 
      
    // Store form name as "imagen" with imagen data
    formData.append("file", imagen, imagen.name);
      
    // Make http post request over api with formData as req
    return this._http.post(this._url + "/imagen/subir", formData)
  }
}
