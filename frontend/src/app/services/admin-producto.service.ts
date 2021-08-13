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

  actualizaCategorias( idProducto: number, categorias : {categorias : string} )  {
    return this._http.post<IadminProducto>(this._url+`/categoria/actualiza/${idProducto}`, categorias);
  }


  eliminaProducto( idProducto: number )  {
    return this._http.delete<IadminProducto>(this._url+`/producto/${idProducto}`);
  }


  subeImagen( idProducto: number, img_file):Observable<any> {
  
    // Create form data
    const formData = new FormData(); 
      
    // Store form name as "imagen" with imagen data
    formData.append("imagen", img_file );
      
    // Make http post request over api with formData as req
    return this._http.post(this._url + `/imagen/subir/${idProducto}`, formData)
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
