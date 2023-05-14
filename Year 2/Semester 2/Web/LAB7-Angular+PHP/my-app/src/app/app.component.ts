import {Component, OnInit, ViewChild} from '@angular/core';
import {MatTableDataSource} from '@angular/material/table';
import {Document} from "./Document";
import {MatPaginator} from "@angular/material/paginator";
import {MatSort} from "@angular/material/sort";
import {MatDialog} from "@angular/material/dialog";
import {DocumentsService} from "./documents.service";
import {CoreService} from "./core/core.service";
import {DocumentAddEditComponent} from "./document-add-edit/document-add-edit.component";
import { ConfirmationDialogComponent } from './confirmation-dialog/confirmation-dialog.component';



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'documents-app';

  displayedColumns: string[] = ['id', 'author', 'title', 'pages', 'types', 'format', 'action'];
  dataSource!: MatTableDataSource<Document>;

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;


  constructor(private _dialog: MatDialog, private ApiSrv: DocumentsService, private _coreService: CoreService){}

  ngOnInit() {
    this.getDocumentsList();
  }

  openAddEditForm(){
    const dialogRef = this._dialog.open(DocumentAddEditComponent);
    dialogRef.afterClosed().subscribe({
      next: (val) => {
        if(val){
          this.getDocumentsList();
        }
      }
    })
  }

  getDocumentsList(){
    this.ApiSrv.getDocuments().subscribe({
      next: (res) => {
        if (res.success === 1) {

          this.dataSource = new MatTableDataSource(res.data);
          this.dataSource.sort = this.sort;
          this.dataSource.paginator = this.paginator;
        }
        else{
          console.error('Error retrieving documents:', res.message);

        }
        },
      error: (err) =>{
        console.log(err);
      }
    });
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  confirmDelete(documentId: string) {
    const dialogRef = this._dialog.open(ConfirmationDialogComponent, {
      data: 'Are you sure you want to delete this document?',
    });

    dialogRef.afterClosed().subscribe((result) => {
      if (result) {
        // User confirmed the deletion, call the deleteFruit method
        this.deleteFruit(documentId);
      }
    });
  }

  deleteFruit(documentId: string){
    this.ApiSrv.deleteDocument(documentId).subscribe({
      next: (res) => {
        this._coreService.openSnackBar("Document deleted!", 'done')
        this.getDocumentsList();
      },
      error: console.log,
    });
  }

  openEditForm(data: Document){
    const dialogRef = this._dialog.open(DocumentAddEditComponent, {
      data,
    });
    dialogRef.afterClosed().subscribe({
      next: (val) => {
        if(val){
          this.getDocumentsList();
        }
      }
    })
  }

}
