connect plocal:../sonatype-work/nexus3/db/component admin admin;

select name, size, last_downloaded    from asset    where format != 'docker'      and last_downloaded < '2020-06-25 00:00:00'    order by size desc;

exit
