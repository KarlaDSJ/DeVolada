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

  // Id del producto a editar
  id_producto_seleccionado = 0;

  set_Producto_seleccionado(idProducto){
    this.id_producto_seleccionado = idProducto;
    console.log("Se seleccionó el producto <" + this.id_producto_seleccionado + ">");
  }
  
  get_Producto_seleccionado(){
    return this.id_producto_seleccionado;
  }



  constructor( private _http: HttpClient ) {}

  daAltaProducto( datosProducto : {correo: string, 
                                   nombre: string, 
                                   precio:number, 
                                   descripcion: string , 
                                   disponibles:number} ): Observable<IadminProducto> {
    return this._http.post<IadminProducto>(this._url+"/producto", datosProducto);
  }

  actualizaProducto( datosProducto : { idProducto: number,
    correo: string, 
    nombre: string, 
    precio:number, 
    descripcion: string , 
    disponibles:number} ): Observable<IadminProducto> {
    let idProducto = datosProducto.idProducto;
    return this._http.patch<IadminProducto>(this._url+"/producto/"+idProducto, datosProducto);
  }

  actualizaCategorias( idProducto: number, categorias : {categorias : string} )  {
    return this._http.post<IadminProducto>(this._url+`/categoria/actualiza/${idProducto}`, categorias);
  }

  // Manda las peticiones para eliminar un producto del sistema
  eliminaProducto( idProducto: number )  {
    // Borra el registro del producto de la BD
    return this._http.delete<IadminProducto>(this._url+`/producto/${idProducto}`);
  }

  // Borra el registro de las imagenes de la BD y los archivos correspondientes del sistema
  eliminaImagenesProducto( idProducto: number){
    return this._http.delete<any>(this._url+`/imagenes/producto/${idProducto}`)
  }

  subeImagenes( idProducto: number, img_files: any[] ):Observable<any> {
  
    // Create form data
    const formData = new FormData(); 

    for( let i=0; i< img_files.length; i++ ){
      formData.append("imagen["+i+"]", img_files[i].file );
    }
      
    // Make http post request over api with formData as req
    return this._http.post(this._url + `/imagenes/subir/${idProducto}`, formData)
  }

}
