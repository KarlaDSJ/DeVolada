import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders  } from '@angular/common/http';
import {HttpParams} from "@angular/common/http";
import { Observable } from 'rxjs';
import { ProductosService } from './productos.service';

export interface IResena {
  idProducto: String;
  correo: String;
  calificacion: number;
  opinion: String;
}

export interface IInfoProducto {
  idProducto: string;
  nombre: String;
  imagen: String;
}

@Injectable({
  providedIn: 'root'
})
export class ResenasService {
  private _url = "http://127.0.0.1:5000";

  infoProducto: IInfoProducto;
  headers = new HttpHeaders().set('Content-Type', 'application/json');

  constructor(private _http: HttpClient) { }

  setInfoProducto(info: IInfoProducto){
    this.infoProducto = info;
  }

  getInfoProducto(): IInfoProducto{
    return this.infoProducto;
  }
  /*
    Crea una reseña para un producto
  */
  crearResenas(idProducto:string, correo:string, calificacion:number, opinion:string) : Observable<IResena[]>{
    /*const params = new HttpParams()
    .set('idProducto', idProducto)
    .set('correo', correo)
    .set('calificacion', calificacion)
    .set('opinion', opinion)
    return this._http.post<IResena[]>(this._url+"/crearResena",  {params})*/
    
    const params = JSON.stringify({
      'idProducto': idProducto,
      'correo': correo,
      'calificacion': calificacion,
      'opinion': opinion
    });
    
    return this._http.post<IResena[]>(this._url+"/crearResena",  params, {headers: this.headers})
  }

   /*
    Regresa todas las reseñas de un producto
  */
    mostrarResenas(idProducto:string): Observable<IResena[]>{
        const params = new HttpParams().set('idProducto', idProducto);
        return this._http.get<IResena[]>(this._url+"/mostrarResenas", { params: params });
    }

  /*
    Regresa las 5 primeras reseñas de un producto
  */
    mostrar5Resenas(idProducto:string): Observable<IResena[]>{
      return this._http.get<IResena[]>(this._url+"/resenas/"+idProducto)
    }
    
}
