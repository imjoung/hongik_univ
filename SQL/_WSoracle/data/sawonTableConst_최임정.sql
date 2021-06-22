DROP table sawon;

CREATE table sawon(
sabun number(3),
saname varchar2(10) CONSTRAINT sawon_saname_nn NOT NULL,
deptno number(3),
sajob varchar2(10),
sapay number(10),
sahire date DEFAULT sysdate,
sasex varchar2(6),
samgr number(3),
CONSTRAINT sawon_sabun_pk PRIMARY KEY (sabun),
CONSTRAINT sawon_deptno_fk FOREIGN KEY (deptno) REFERENCES dept(deptno),
CONSTRAINT sawon_sasex_ck CHECK (sasex in ('남자','여자')),
CONSTRAINT sawon_samgr_fk FOREIGN KEY (samgr) REFERENCES sawon(sabun)
);
