# -*- coding: utf-8 -*-

import json, logging

from django.test import TestCase


log = logging.getLogger(__name__)
log.debug( 'logging ready' )
TestCase.maxDiff = None


class RootUrlTest( TestCase ):
    """ Checks root urls. """

    def test_root_url_no_slash(self):
        """ Checks '/root_url'. """
        response = self.client.get( '' )  # project root part of url is assumed
        self.assertEqual( 302, response.status_code )  # permanent redirect
        redirect_url = response._headers['location'][1]
        self.assertEqual(  '/info/', redirect_url )

    def test_root_url_slash(self):
        """ Checks '/root_url/'. """
        response = self.client.get( '/' )  # project root part of url is assumed
        self.assertEqual( 302, response.status_code )  # permanent redirect
        redirect_url = response._headers['location'][1]
        self.assertEqual(  '/info/', redirect_url )

    # end class RootUrlTest()


# class EntryTest( TestCase ):
#     """ Checks entry-data construction. """

#     def test_short_top_summary(self):
#         """ Checks first line. """
#         from mp_vl_app.lib import views_entry_helper as helper
#         for (i, entry) in enumerate( SAMPLE_ENTRIES ):
#             log.debug( f'i, ``{i}``; entry-title, ``{entry["title"]}``' )
#             if i == 0:
#                 log.debug( 'i is 0' )
#                 self.assertEqual( 'Racial Violence', helper.process_data(entry)['summary_first_line'] )
#             elif i == 1:
#                 self.assertEqual( '1919 April 8', helper.process_data(entry)['summary_first_line'] )
#             elif i == 2:
#                 self.assertEqual( '1915 July 29', helper.process_data(entry)['summary_first_line'] )
#             elif i == 3:
#                 self.assertEqual( '1922 June 23', helper.process_data(entry)['summary_first_line'] )
#             elif i == 4:
#                 self.assertEqual( '1915 August 16', helper.process_data(entry)['summary_first_line'] )

#     ## end class EntryTest()


SAMPLE_ENTRIES = [
    {
        '_id': '57a01088f70fce7140d30662',
        'aggressors': [],
        'date': {'day': 3, 'month': 11.0, 'year': 1910},
        'date_display': '1910 November 3',
        'description': 'On November 2, 1910, Effie Greer Henderson lay dead on her porch, shot once in the back and once in the head. She was survived by her husband, Lemuel Kenneth Henderson and their five children. Soon after the murder, a posse searched for the assailant in the Texas hill country of Edwards County. The next day they arrested Mexican national Antonio Rodríguez. The local sheriff placed Rodríguez in the Edwards County Jail. That afternoon, a local mob removed the accused from his prison cell, bound him to a barbed mesquite tree, and burned him alive. The lynching of Antonio Rodríguez triggered diplomatic tensions between the United States and Mexico and made Rocksprings the subject of international newspaper headlines. The failure of the Texas judicial system to investigate and convict the Rocksprings vigilantes sparked protests in Mexico. This case is the most widely-noted lynching of an ethnic Mexican in Texas.',
        'entryCategory': 'Racial Violence',
        'id_clean': '57a01088f70fce7140d30662',
        'is_old_id': 1.0,
        'latitude': 30.0158,
        'locationRationale': 'County Jail where Rodriguez removed from police custody address is on same block as County Courthouse (101 E Main St, Rocksprings, TX 78880). The Lat and Long 30.0158° N, 100.2054° W is the general location for Rocksprings, Texas',
        'longitude': -100.2054,
        'metadata': {'lastEditedAt': '2019-06-12 19:30:55.738000',
        'lastEditedBy': '57a02348f70fce7140d3067a'},
        'primarySources': [''],
        'status': 'IN_POOL',
        'title': 'Lynching of Antonio Rodríguez in Rocksprings November 3, 1910',
        'victims': []
    },
    {
        '_id': '5a51180308813b00015f7454',
        'aggressors': [],
        'date': {'day': 8, 'month': 4.0, 'year': 1919},
        'date_display': '1919 April 8',
        'description': 'In 1919, Concepcion García, a Mexican national, was living in Texas in order to attend school. That same year, Lt. Robert L. Gulley of the US Cavalry patrolled the US-Mexico border. Concepcion became ill, and attempted to return home on April 8. While crossing the river back to Mexico on a raft, the young girl, her mother Maria, and her aunt found themselves under fire. Lt. Gulley shot at the group killing Concepcion.  The lieutenant’s firing at an unarmed group necessitated an investigation, and on April 28, 1919, a court-martial tried and sentenced Lt. Gulley, dismissing him from military service. However, President Woodrow Wilson, reversed the findings and restored him to duty in September 1919. \nTeodoro García and Maria Apolinar Garza charged the United States with the wrongful death of their daughter and denial of justice. Hearing the case on December 3, 1926, the US-Mexico General Claims Commission found that states should be punished for “such offenses as unnecessary shooting across the border without authority.”  The commission obligated the US government to pay an indemnity of $2,000 without interest on behalf of Teodoro García and Maria Apolinar García. This case is just one of relatives receiving indemnities from the United States government for the wrongful death of their relatives and denial of justice.\n',
        'id_clean': '5a51180308813b00015f7454',
        'is_old_id': 1.0,
        'latitude': 26.235715,
        'locationRationale': 'Claim states that Robert Gulley shot at the family as the crossed the Rio Grande near Havana Texas. Placed a pin on google maps where there is a bend in the Rio Grande that nears Havana.',
        'longitude': -98.522327,
        'metadata': {'lastEditedAt': '2018-01-06 21:34:33.717000', 'lastEditedBy': '57a02348f70fce7140d3067a'},
        'primarySources': ['Teodoro García and M.A. Garza (United Mexican States) v. United States of America (1926)'],
        'status': 'IN_POOL',
        'title': 'Young Concepcion García Shot and Killed by US Soldier in Rio Grande, 1919',
        'victims': [
            {
            'age': 'Child ',
            'ethnicity': [],
            'gender': 'Female',
            'name': 'Concepcion García',
            'nationality': 'Mexican',
            'race': []
            },
            {
            'ethnicity': [],
            'gender': 'male',
            'name': 'Teodoro García (father of Concepcion)',
            'nationality': 'Mexican',
            'race': []
            },
            {
            'ethnicity': [],
            'gender': 'female',
            'name': 'Maria Apolinar García (mother of Concepcion)',
            'nationality': 'Mexican',
            'race': []
            }
        ]
    },
    {
        '_id': '57a24820f70fce2911f7ab85',
        'aggressors': [],
        'date': {'day': 29, 'month': 7.0, 'year': 1915},
        'date_display': '1915 July 29',
        'description': 'On July 29, 1916, Sheriff Frank Carr and Ranger Daniel Hinojosa arrested Rodolfo Muñoz (also referred to as Adolfo Muñoz or Rudolfo Muñiz) in San Benito after local farmers accused him of membership in a local gang. \n\n\nAfter Carr and Hinojosa took Muñoz into police custody, they transported Muñoz to the county jail in Brownsville under the cover of night. The next morning, Muñoz’s body was found riddled with bullets and hanging from a tree on the road between San Benito and Brownsville. At the time of his death, Muñoz had not yet been charged with a single crime. \n\n\nCarr and Hinojosa claimed that a group of eight armed masked men had stopped the car on the way to the county jail, forced Muñoz out of police custody, and lynched him. Some sources claim that Carr and Hinojosa had killed Muñoz themselves and fabricated the lynching to escape responsibility. \n\n\nAfterwards, the story of the lynching caused ethnic Mexican suspects to refuse to cooperate with law enforcement for fear that they too would be killed without due process. \n\n\n',
        'id_clean': '57a24820f70fce2911f7ab85',
        'is_old_id': 1.0,
        'latitude': 25.907467,
        'locationRationale': 'This is the site of what google calls the "Old County Jail." It\'s likely where the officers were supposed to bring Muñoz. I chose this location rather than a spot along the road because this location is more certain.',
        'longitude': -97.49497,
        'metadata': {'lastEditedAt': '2019-06-13 14:42:17.906000', 'lastEditedBy': '57a02348f70fce7140d3067a'},
        'primarySources': [
            '“Border justice is quick and certain: Masked men take Mexican from officer and lynch him to nearby tree.” The Daily Bulletin. (Brownwood, TX), July 29, 1915, p. 1.',
            '“Masked men hold up Deputy Sheriff near Brownsville, with rifles.” San Antonio Light. (San Antonio, TX), July 29, 1915, p. 1.',
            '“Mob takes man from Deputy and lynch him.” The Daily Advocate. (Victoria, TX), July 30, 1915, p. 4.',
            'Pierce, Frank Cushman. A Brief History of the Lower Rio Grande Valley. George Banta publishing Company, 1917, p. 90.',
            '“Proceedings of the Joint Committee of the Senate and the House in the Investigation of the Texas State Ranger Force,'
        ],
        'secondarySources': [
            'Carrigan, William D., and Clive Webb. *Forgotten Dead: Mob Violence against Mexicans in the United States*, 1848-1928. 1 edition. Oxford: Oxford University Press, 2013, appendix A.',
            'Johnson, Benjamin Heber. *Revolution in Texas: How a Forgotten Rebellion and Its Bloody Suppression Turned Mexicans into Americans.* New Haven: Yale University Press, 2005, p. 86-7.',
            'Weber, John William III. ',
            'Ribb, Richard. “La Rinchada: Revolution, Revenge, and the Rangers, 1910-1920.” In *War along the Border: The Mexican Revolution and Tejano Communities*, edited by Arnoldo de León, 56-106. College Station: Texas A&M University Press, 2012, p. 68, 118.'
      ],

        'status': 'IN_POOL',
        'title': 'Lynching of Rodolfo Muñoz in San Benito, 1915',
        'victims': [
            {
            'ethnicity': ['Mexican'],
            'gender': 'Male',
            'name': 'Rodolfo Muñoz',
            'nationality': 'United States ',
            'race': []
            }
        ]
    },
    {
        '_id': '59bdcd2508813b00015f7391',
        'aggressors': [],
        'date': {'day': 23, 'month': 6.0, 'year': 1922},
        'date_display': '1922 June 23',
        'description': 'Reports of Warren Lewis’s lynching in New Dacus, Texas on June 23, 1922 circulated among regional newspapers in the days after. These accounts addressed little of the crime for which the 18-year-old was accused—allegedly, for “attack[ing] a young married white woman”—but provided, instead, more substantially details of the public hanging itself, held before a crowd of at least 300 spectators, including “scores of negroes” to whom Lewis spoke before his death. The United Press shared that Lewis told the assembled crowd to learn from his example so that “members of his race [would] stay in their place” and “to do the right thing” with regards to keeping peace among residents of the Montgomery County town.  ',
        'id_clean': '59bdcd2508813b00015f7391',
        'is_old_id': 1.0,
        'latitude': 30.446996,
        'locationRationale': 'The town of New Dacus referenced in the historical newspapers likely corresponds with the present-day town of Dacus, Texas in Montgomery County. ',
        'longitude': -95.792938,
        'metadata': {'lastEditedAt': '2018-01-04 16:52:40.698000', 'lastEditedBy': '57a02348f70fce7140d3067a'},
        'primarySources': [
            '“New Dacus Quiet After Lynching of Young Negro.” Victoria Advocate. Victoria, Texas. June 25, 1922. Page 1.  ',
            '“Negro Is Lynched at New Dacus for Attack on Woman.” Wichita Daily Times. Wichita Falls, Texas. June 24, 1922. Page 1. ',
            '“Negro is Hanged.” Fort Wayne News Sentinel. Fort Wayne, Indiana. June 24, 1922. Page 14. ',
            '“Telegraph Tabloids.” Lincoln Star. Lincoln, Nebraska. June 24, 1922. Page 5. ',
            '“Negro to Be Hanged Addresses Fellows.” Joplin Globe. Joplin, Missouri. June 24, 1922. Page 1. ',
            'National Association for the Advancement of Colored People. 13th Annual Report for the Year 1922. New York: NAACP, 1923. Page 32. '
        ],
        'status': 'IN_POOL',
        'title': 'Lynching of Warren Lewis in New Dacus, 1922',
        'victims': [
            {
            'age': '18-years-old',
            'ethnicity': [],
            'name': 'Warren Lewis',
            'race': ['Black']
            }
        ]
    },
    {
        '_id': '57a01e90f70fce7140d30675',
        'aggressors': [],
        'date': {'day': 16, 'month': 8.0, 'year': 1915},
        'date_display': '1915 August 16',
        'description': 'On August 16, 1915, following reports of alleged bandits in the area, a U.S. Army patrol made its way to the border to investigate near the Progreso River Banks. At 9:30 p.m., shooting began. Thirteen soldiers were killed, including Corporal Wellman of the Twelfth United States Cavalry. In addition, Lieutenant Roy Henry and a Private Jackson were also wounded. The *Brownsville Herald* wrote the next morning that “all reports indicate that the firing was from the Mexican side [of the border].” The fighting lasted 20 minutes and took place in total darkness. Eyewitnesses later claimed that 100-200 Mexicans mobilized along the border in this area in preparation for the attack and, they suspected, an invasion of the American territory that would involve revolutions leading up to Harlingen. Within 24 hours over 800 troops, including U.S. Soldiers and Texas Rangers, flooded the area.',
        'id_clean': '57a01e90f70fce7140d30675',
        'is_old_id': 1.0,
        'latitude': 26.064854,
        'locationRationale': 'Event reported as happening near the border along the Progreso River Banks by primary sources.\nUpdate (Nnamdi)\nFrom the Museum of South Texas History and a dissertation from 1983, I found a map and some other information indicating the location of the event, as described happening at Mercedes Pump. Mercedes Pump was apparently 2 and a half miles up the Rio Grande in a town now called Rio Rico.  Mercedes Pump was apparently next to a bridge, the Rio Rico Bridge, which was demolished as of 1941. The town of Rio Rico, in modern day Progreso near Mercedes as well, does not exist anymore. The map from the dissertation gives me the grooves of where the pump was, but I am still a bit confused as to where it is exactly. I perhaps wanted to check with Felicia and Professor Martinez first to see where they think. ',
        'longitude': -97.969925,
        'metadata': {'lastEditedAt': '2019-06-20 21:42:14.419000', 'lastEditedBy': '57a02348f70fce7140d3067a'},
        'primarySources': [
            '“Herald Democrat August 17, 1915 — Colorado Historic Newspapers Collection,” accessed July 7, 2016, https://www.coloradohistoricnewspapers.org/cgi-bin/colorado?a=d&d=THD19150817-01.2.25#',
            '“Brownsville Herald, August 17, 1915\u202f: Front Page,” accessed July 7, 2016, http://newspaperarchive.com/us/texas/brownsville/brownsville-herald/1915/08-17/',
            'San Antonio Express. (San Antonio, Tex.), Vol. 50, No. 229, Ed. 1 Tuesday, August 17, 1915, newspaper, August 17, 1915; San Antonio, Texas. (texashistory.unt.edu/ark:/67531/metapth432190/m1/1/: accessed July 6, 2016),University of North Texas Libraries, The Portal to Texas History, texashistory.unt.edu; crediting Abilene Library Consortium.',
            'Frank Cushman Pierce, A Brief History of the Lower Rio Grande Valley (Wisconsin: The Collegiate Press, 1917), 92'
        ],
        'secondarySources': ['United States Congress Senate Committee on Foreign Relations, Investigation of Mexican Affairs: Hearing Before a Subcommittee of the Committee on Foreign Relations, United States Senate, Sixty-Sixth Congress, First[-Second] Session, Pursuant to S. Res. 106, Directing the Committee on Foreign Relations to Investigate the Matter of Outrages on Citizens of the United States in Mexico (U.S. Government Printing Office, 1919).'],
        'status': 'IN_POOL',
        'title': 'Thirteen US Soldiers killed in cross border shootout on Rio Grande, 1915',
        'victims': [
            {
                'ethnicity': [],
                'name': 'Corporal Wellman ',
                'occupation': 'Twelfth United States Cavalry',
                'race': ['Anglo']
            }
        ]
    }
]  # end of SAMPLE_ENTRIES
