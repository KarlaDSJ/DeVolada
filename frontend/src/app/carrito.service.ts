import { Injectable } from '@angular/core';
import {HttpParams} from "@angular/common/http";
import { Observable } from 'rxjs'; // Ayuda a ver el rastro de la peticion
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

export interface ICarrito {
  idCarrito: Number;
  productos: {
    idProducto: Number
  }[]
}

export interface IProductoCarrito{
  idProducto: number,
  precio: number,
  nombre: string, 
  disponibles: number,
  cantidad: number, 
  imagenes: {
    imagen: string
  }[]
}


@Injectable({
  providedIn: 'root'
})
export class CarritoService {

  private _url = "http://127.0.0.1:5000";
  
  constructor( private _http: HttpClient ) { }

  crearCarrito(): Observable<ICarrito>{
    return this._http.post<ICarrito>(this._url+"/carrito",{})
  }

  obtenerProductos(idCarrito) : Observable<IProductoCarrito[]>{
    return this._http.get<IProductoCarrito[]>(`${this._url}/contener?idCarrito=${idCarrito}`)
  }
}
