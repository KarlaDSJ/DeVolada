import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import 'rxjs/add/observable/throw';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/do';

interface IProducto {
  id: String;
  correo: String;
  precio: number;
  nombre: String;
  descripcion: String;
  vendidos: number;
  disponibles: number;
  imagenes: String[];
}

@Injectable({
  providedIn: 'root'
})
export class ProductosService {
  private _url = "http://127.0.0.1:5000";

  constructor(private _http: HttpClient) { }

  getProductos(): Observable<IProducto[]>{
    return this._http.get<IProducto[]>(this._url+"/productos");
  }

  private handleError(err: HttpErrorResponse){
    return Observable.throw(err.message);
  }
}
