create table dept(
deptno number(3) constraint dept_deptno_nn not null,
dname varchar2(10),
loc varchar2(10));

//

create table dept(
deptno number(3) constraint dept_deptno_uq unique,
dname varchar2(10),
loc varchar2(10));