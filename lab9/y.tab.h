
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     CST = 258,
     VERIFY = 259,
     YES = 260,
     NO = 261,
     PRINT = 262,
     VAR = 263,
     READ = 264,
     RETURN = 265,
     LIST = 266,
     GO = 267,
     AS = 268,
     WITH = 269,
     PLUS = 270,
     MINUS = 271,
     MUL = 272,
     DIV = 273,
     MOD = 274,
     ASSIGN = 275,
     IS = 276,
     GR = 277,
     GRE = 278,
     LS = 279,
     LSE = 280,
     AND = 281,
     OR = 282,
     NOT = 283,
     DOT = 284,
     DOTS = 285,
     SEMI_COL = 286,
     OPEN_BRK = 287,
     CLOSED_BRK = 288,
     BOOL1 = 289,
     IDENTIFIER1 = 290,
     DIGIT1 = 291,
     NR1 = 292,
     CHAR1 = 293,
     STR1 = 294
   };
#endif
/* Tokens.  */
#define CST 258
#define VERIFY 259
#define YES 260
#define NO 261
#define PRINT 262
#define VAR 263
#define READ 264
#define RETURN 265
#define LIST 266
#define GO 267
#define AS 268
#define WITH 269
#define PLUS 270
#define MINUS 271
#define MUL 272
#define DIV 273
#define MOD 274
#define ASSIGN 275
#define IS 276
#define GR 277
#define GRE 278
#define LS 279
#define LSE 280
#define AND 281
#define OR 282
#define NOT 283
#define DOT 284
#define DOTS 285
#define SEMI_COL 286
#define OPEN_BRK 287
#define CLOSED_BRK 288
#define BOOL1 289
#define IDENTIFIER1 290
#define DIGIT1 291
#define NR1 292
#define CHAR1 293
#define STR1 294




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;


