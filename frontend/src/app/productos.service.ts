import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {HttpParams} from "@angular/common/http";
import { Observable } from 'rxjs';

export interface IProducto {
  idProducto: String;
  correo: String;
  precio: number;
  nombre: String;
  descripcion: String;
  vendidos: number;
  disponibles: number;
  imagenes: {
    imagen: String
  }[];
  categorias: {
    categoria: String
  }[];
}

@Injectable({
  providedIn: 'root'
})
export class ProductosService {
  private _url = "http://127.0.0.1:5000";

  constructor(private _http: HttpClient) { }

  headers = new HttpHeaders().set('Content-Type', 'application/json');

  /*
    Nos regresa todos los productos
  */
  getProductos(): Observable<IProducto[]>{
    return this._http.get<IProducto[]>(this._url+"/productos")
  }

  /*
    Nos el top 5 de productos más vendidos, en caso de no ser posible 
    nos regresa los productos agregados recientemente 
  */
  getTop5(): Observable<IProducto[]>{
    return this._http.get<IProducto[]>(this._url+"/producto/top5");
  }

  /*
    Busca productos por categoria y/o por nombre
  */
  searchProductos(categoria:string, nombre:string): Observable<IProducto[]>{
    const params = new HttpParams()
      .set('nombre', nombre)
      .set('categoria', categoria);

    return this._http.get<IProducto[]>(this._url+"/producto/buscar", {params});
  }

  /*
    Nos regresa la informacion de un producto
  */
  getProducto(id:number): Observable<IProducto>{
    return this._http.get<IProducto>(this._url+"/producto/"+id);
  }

  /*
    Nos regresa la informacion de un producto
  */
  getListaProductos(ids:number[]): Observable<IProducto[]>{
    const params = JSON.stringify({
      "ids": ids
    });
    return this._http.post<IProducto[]>(this._url+"/producto/lista", params, {headers: this.headers});
  }
}
