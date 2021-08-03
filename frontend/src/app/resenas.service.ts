import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import {HttpParams} from "@angular/common/http";
import { Observable } from 'rxjs';
import { ProductosService } from './productos.service';

export interface IResena {
  idProducto: String;
  correo: String;
  calificacion: number;
  opinion: String;
}

@Injectable({
  providedIn: 'root'
})
export class ResenasService {
  private _url = "http://127.0.0.1:5000";

  constructor(private _http: HttpClient) { }

  /*
    Nos regresa todos los productos
  */
  crearResenas(idProducto:string, correo:string, calificacion:number, opinion:string) : Observable<IResena[]>{
    const params = new HttpParams()
    .set('idProducto', idProducto)
    .set('correo', correo)
    .set('calificacion', calificacion)
    .set('opinion', opinion)
    return this._http.post<IResena[]>(this._url+"/crearResena",  {params})
  }

   /*
    Nos regresa la informacion de un producto
  */
    mostrarResenas(idProducto:string): Observable<IResena[]>{
        const params = new HttpParams().set('idProducto', idProducto);
        return this._http.get<IResena[]>(this._url+"/mostrarResenas", { params: params });
    }

}
