DROP table dept

CREATE table dept(
deptno number(3),
dname varchar2(10),
loc varchar2(10),
CONSTRAINT dept_deptno_pk PRIMARY KEY (deptno),
CONSTRAINT dept_dname_uq UNIQUE (dname));