%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define YYDEBUG 1 

int yylex();
void yyerror(char *s);
%}

%token CST
%token VERIFY
%token YES
%token NO
%token PRINT
%token VAR
%token READ
%token RETURN
%token LIST
%token GO
%token AS
%token WITH

%token PLUS
%token MINUS
%token MUL
%token DIV
%token MOD
%token ASSIGN
%token IS 
%token GR
%token GRE
%token LS
%token LSE 
%token AND 
%token OR
%token NOT 
%token DOT

%token DOTS 
%token SEMI_COL
%token OPEN_BRK 
%token CLOSED_BRK 

%token BOOL1
%token IDENTIFIER1
%token DIGIT1
%token NR1
%token CHAR1
%token STR1 

%start program 

%%
program : declist programC ;
programC : /* empty */ | stmtlist ;
declist : declaration SEMI_COL declistC ;
declistC : /* empty */ | declist ;
declaration : type IDENTIFIER1 ;
type : VAR | CST ;
stmtlist : stmt SEMI_COL stmtlistC ;
stmtlistC : /* empty */ | stmtlist ;
stmt : simplestmt | structstmt ;
simplestmt : assignstmt | iostmt ;
assignstmt : IDENTIFIER1 ASSIGN expr ;
expr : term exprC ;
exprC : /* empty */ | exprOp expr ;
exprOp : PLUS | MINUS ;
term : factor termC ;
termC : /* empty */ | termOP term ;
termOP : MUL | DIV | MOD ;
factor : IDENTIFIER1 | NR1 ;
iostmt : READ IDENTIFIER1 | PRINT IDENTIFIER1 ;
structstmt : ifstmt | forstmt ;
ifstmt : VERIFY cond DOTS YES DOTS stmtlist ifstmtC ;
ifstmtC : /* empty */ | NO DOTS stmtlist ;
cond : term rel term ;
rel : IS | GR | GRE | LS | LSE ;
forstmt : GO assignstmt AS cond WITH assignstmt DOTS stmt ;
%%
void yyerror(char *s)
{	
	printf("%s\n",s);
}

extern FILE *yyin;

int main(int argc, char **argv)
{
	if(argc>1) yyin :  fopen(argv[1],"r");
	if(argc>2 && !strcmp(argv[2],"-d")) yydebug: 1;
	if(!yyparse()) fprintf(stderr, "\tO.K.\n");
}
