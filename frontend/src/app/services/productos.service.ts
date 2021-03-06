import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
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
  categoria: ICategoria[];
}

export interface ICategoria {
  categoria: String
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
    const params = JSON.stringify({
      'nombre': nombre,
      'categoria': categoria
    });

    return this._http.post<IProducto[]>(this._url+"/producto/buscar", params, {headers: this.headers});
  }

   /*
    Obtiene todos los productos de un vendedor a partir de su correo.
  */
  obtenProductosVendedor(correo:string): Observable<IProducto[]>{
    return this._http.get<IProducto[]>(this._url+"/productos/vendedor/" + correo );
  }

  /*
    Nos regresa la informacion de un producto
  */
  getProducto(id:number): Observable<IProducto>{
    return this._http.get<IProducto>(this._url+"/producto/"+id);
  }

  /*
    Nos regresa los archivos de imagenes de un producto
  */
  getImagenes(id:number): Observable<IProducto>{
    return this._http.get<IProducto>(this._url+"/imagen/"+id);
  }


  // Regresa un json con las imagenes del producto codificadas en base64 URI.
  getImagenesDecodificadas( idProducto ){
    return this._http.get(this._url +`/imagenes/producto/${idProducto}`)
  }

  // Regresa un json con la primer imagen del producto codificada en base64 URI.
  getImagenDecodificada( idProducto ): Promise <any> {
    return this._http.get(this._url +`/imagen/producto/${idProducto}`).toPromise()
  }

  /*
    Nos regresa todas las categorías
  */
  getCaregoria(): Observable<ICategoria[]>{
    return this._http.get<ICategoria[]>(this._url+"/categorias");
  }

}
