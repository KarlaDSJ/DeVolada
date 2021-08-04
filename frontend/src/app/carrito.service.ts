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

export interface IContenerProducto{
  idProducto: number,
  idCarrito: number,
  cantidad: number
}

export interface IMensaje{
  msg: string
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

  agregarCarrito(idProducto:number, idCarrito:number): Observable<IMensaje>{
    return this._http.post<IMensaje>(`${this._url}/contener`, {idProducto, idCarrito})
  }

  obtenerProductos(idCarrito:number) : Observable<IProductoCarrito[]>{
    return this._http.get<IProductoCarrito[]>(`${this._url}/contener?idCarrito=${idCarrito}`)
  }

  cambiarCantidad(idProducto:number, idCarrito:number, cantidad:number): Observable<IContenerProducto>{
    const params={idProducto, idCarrito} 
    return this._http.put<IContenerProducto>(`${this._url}/contener`,{cantidad}, {params})
  }

  eliminarProducto(idProducto:number, idCarrito:number): Observable<IMensaje>{
    const params={idProducto, idCarrito} 
    return this._http.delete<IMensaje>(`${this._url}/contener`, {params})
  }

  obtenerTotal(idCarrito:number): Observable<number> {
    return this._http.get<number>(`${this._url}/totalCarrito?idCarrito=${idCarrito}`)
  }

  limpiarCarrito(idCarrito:number): Observable<IMensaje>{
    return this._http.delete<IMensaje>(`${this._url}/limpiarCarrito?idCarrito=${idCarrito}`)
  }
}
