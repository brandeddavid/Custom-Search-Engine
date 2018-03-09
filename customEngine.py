from yattag import Doc, indent


def createXML():
    doc, tag, text = Doc().tagtext()
    id='wvsnl7ztkuw'

    text('<?xml version="1.0" encoding="UTF-8" ?>\n')
    with tag('CustomSearchEngine', id=id):
        with tag('Title'):
            text('Custom Search Engine')
        with tag('Context'):
            with tag('BackgroundLabels'):
                with tag('Label', name='_cse_'+id, mode='FILTER'):
                    pass
                with tag('Label', name='_cse_exclude_' + id, mode='ELIMINATE'):
                    pass
            with tag('LookAndFeel', nonprofit='false', element_layout='8', theme='7', custom_theme='true', text_font='Arial sans-serif', element_branding='show', enable_cse_thumbnail='true', promotion_url_length='full', ads_layout='1'):
                with tag('Logo'):
                    pass
                with tag('Colors'):
                    pass
                with tag('Promotions'):
                    pass
                with tag('SearchControls'):
                    pass
                with tag('Results'):
                    pass
            with tag('AdSense'):
                pass
            with tag('EnterpriseAccount'):
                pass
            with tag('ImageSearchSettings', enable='false'):
                pass
            with tag('autocomplete_settings'):
                pass
            with tag('sort_by_keys', label='Relevance', key=''):
                pass
            with tag('sort_by_keys', label='Date', key='date'):
                pass
            with tag('cse_advance_settings', enable_speech='true'):
                pass

    result = indent(doc.getvalue(), indentation=' '*4, newline='\r\n')

    return result


def writeToFile(fileName, XMLFile):

    with open(fileName, 'w') as outFile:

        outFile.writelines(XMLFile)


def main():

    writeToFile('customEngine.xml', createXML())


if __name__ == '__main__':

    main()